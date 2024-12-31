import asyncio
import aiofiles


async def read_file(file_name):

    print(f"Reading : {file_name}")
    async with aiofiles.open(file_name, mode='r') as file:
        content = await file.read()
    print(f"finished reading: {file_name}")
    return content


async def write_combined_file(output_file, contents):
    print(f"Writing contents of the file in new file:")
    async with aiofiles.open(output_file, mode='w') as file:
        for content in contents:
            await file.write(content + "\n")
    print(f"writing completed!")


async def main():
    input_files = ["file1.txt", "file2.txt", "file3.txt"]
    output_file = "output.txt"
    read_tasks = [read_file(file) for file in input_files]
    contents = await asyncio.gather(*read_tasks)
    await write_combined_file(output_file, contents)


asyncio.run(main())
