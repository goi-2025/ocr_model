import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(2)  # Simulate async delay
    print(f"How are you, {name}?")

# Run the async function
async def main():
    await greet("Alice")



#asyncio.run(main())
