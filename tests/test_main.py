api_key = "api_key"
model_name = "gpt-3.5-turbo"

from chatgptdevfriendly.v1 import ChatGptSmartClient


chatgptsmtclient = ChatGptSmartClient(api_key=api_key, model=model_name, log_info=True)

for _ in range(10):
    chatgptsmtclient.query("List the top 10 upcoming startups in India?")
    chatgptsmtclient.query(
        "Ok thanks, can you giv me the valuation of these startups in tabuar format"
    )

chatgptsmtclient.dump_context_to_a_file("context")
chatgptsmtclient.load_context_from_a_file("context")

chatgptsmtclient.print_metrics()
