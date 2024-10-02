link = input("\n\n\nInsert list (space-separated): ").split()
connect = input("\n\n\nAddition: ")

new_list = [item + connect for item in link]

def split_into_chunks(lst, chunk_size=20):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

chunked_lists = split_into_chunks(new_list)

for idx, chunk in enumerate(chunked_lists, 1):
    print("\n-----------")
    print(f'List {idx}: [{", ".join(chunk)}]')
    print(f"\nCount of items in List {idx}: {len(chunk)}")