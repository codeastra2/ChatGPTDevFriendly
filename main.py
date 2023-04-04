import openai
openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are useful assistant"},
            {"role": "user", "content": "Can you tell top 10 startups in India"},
		{"role": "assistant",   "content": "1. Flipkart \n2. Ola Cabs \n3. Paytm \n4. BYJU's \n5. Swiggy \n6. Zomato \n7. Udaan \n8. Freshworks \n9. Nykaa \n10. Policybazaar"},
		 {"role": "user", "content": "That is good but can you tell top 10 early stage strtups? some of these re late stage...."},
		
        ]
)
