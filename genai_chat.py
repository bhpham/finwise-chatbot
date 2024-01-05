import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from vertexai.language_models import ChatModel, InputOutputTextPair
import vertexai
import json

load_dotenv()


class GenAiChat:
    def __init__(self) -> None:
        self.project_id = os.getenv("PROJECT_ID")
        self.location_id = os.getenv("LOCATION_ID")
        self.model_id = os.getenv("MODEL_ID")
        self.service_account_file_path = os.getenv("SERVICE_ACCOUNT_FILE_PATH")
        self.scopes = os.getenv("SCOPES").split(",")
        self.candidate_count = int(os.getenv("CANDIDATE_COUNT"))
        self.max_output_tokens = int(os.getenv("MAX_OUTPUT_TOKENS"))
        self.temperature = float(os.getenv("TEMPERATURE"))
        self.top_p = float(os.getenv("TOP_P"))
        self.top_k = int(os.getenv("TOP_K"))

    def get_credentials(self) -> service_account.Credentials:
        credentials = service_account.Credentials.from_service_account_file(
            self.service_account_file_path, scopes=self.scopes
        )
        return credentials

    def send_chat(self, context: str, prompt: str) -> tuple:
        credentials = self.get_credentials()
        vertexai.init(
            project=self.project_id, location=self.location_id, credentials=credentials
        )
        parameters = {
            "candidate_count": int(self.candidate_count),
            "max_output_tokens": int(self.max_output_tokens),
            "temperature": float(self.temperature),
            "top_p": float(self.top_p),
            "top_k": int(self.top_k),
        }

        model = ChatModel.from_pretrained(self.model_id)
        chat = model.start_chat(
            context=f"{context}",
            examples=self.build_examples()
        )
        response = chat.send_message(f"""{prompt}""", **parameters)
        
        return response, chat.message_history

    def build_examples(self) -> list[InputOutputTextPair]:
        with open("examples.json") as examples_file:
            examples = json.load(examples_file)

        input_output_text_pairs = []

        for example in examples:
            input_output_text_pairs.append(
                InputOutputTextPair(
                    input_text=example["input"], output_text=example["output"]
                )
            )        
        
        return input_output_text_pairs
