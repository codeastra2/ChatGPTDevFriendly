api_key = "openai_api_key"
model_name = "gpt-3.5-turbo"

from main import ChatGptSmartClient


chatgptsmtclient = ChatGptSmartClient(api_key=api_key, model=model_name, log_info=True)

print(chatgptsmtclient.query("List the top 10 upcoming startups in India?"))
print(chatgptsmtclient.query("Ok thanks, can you giv me the valuation of these startups in tabuar format"))

chatgptsmtclient.print_metrics()