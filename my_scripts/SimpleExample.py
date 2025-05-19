from metagpt.roles import Engineer

async def main():
    engineer = Engineer()
    prompt = "Write a Python function that sorts a list of numbers."
    result = await engineer.run(prompt=prompt)
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())