from src.chains.engines.cerberus_web_client import CerberusWebClient


class TivTaam(CerberusWebClient):
    @property
    def username(self):
        return "TivTaam"
