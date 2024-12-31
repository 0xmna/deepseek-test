from openai import OpenAI

client = OpenAI(api_key="sk-9dedc9dd752d491a8c1a479134e7ccc", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名拥有20年编程经验的高级工程师，精通Python、Java、JavaScript等多种编程语言，擅长解决复杂问题，并具有良好的沟通能力和团队合作精神。"},
        {"role": "user", "content": "我现在需要写一个python自动化脚本，但是遇到了cloudflare点击不了，你能帮我解决这个问题吗？"},
    ],
    stream=False
)

print(response.choices[0].message.content)
