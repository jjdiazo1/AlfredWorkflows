# Kaomoji Search Workflow

This Alfred workflow allows you to search through a collection of over **100+ kaomojis** and put them directly to your cursor is.

<img width="646" alt="Screenshot 2024-10-12 at 4 37 52 PM" src="https://github.com/user-attachments/assets/0cc05cf3-57eb-400b-b92a-2d8ba87dc457">

## Keyword

- `k {query}`

Start typing `k` followed by a search query (e.g., "happy", "sad", etc.) to filter through the available kaomojis

## How to Use

1. Activate Alfred and type `k` followed by a keyword to search for kaomojis.
2. As you type, the list will narrow down to show relevant kaomojis.
3. Press `Enter` on the desired kaomoji to put it directly where your cursor is.

## Example

Type `k happy` to find kaomojis like `٩(◕‿◕｡)۶`. Press `Enter` and it will directly be put wherever your cursor is.

## To add more Kaomojis

1. Refer to the [Script.py](https://github.com/jjdiazo1/AlfredWorkflows/blob/290509c9cad6b6e46d658427a50f276889e060ac/Kaomoji/Script.py) file and put them in this line, in the dictionary. 

```python
# A list of kaomojis with their descriptions
kaomojis = [
    {"face": "( ͡° ͜ʖ ͡°)", "name": "Lenny Face"},
    {"face": "¯\\_(ツ)_/¯", "name": "Shrug"},
    {"face": "(╯°□°）╯︵ ┻━┻", "name": "Table Flip"},
    {"face": "(•_•)", "name": "Cool Guy"},
    {"face": "٩(◕‿◕｡)۶", "name": "Happy Dance"},
    # Add more kaomojis as needed
]
```

2. Then copy that modified file, go to the alfred workflow and click on the Script Filter:

> <img width="301" alt="Screenshot 2024-10-12 at 4 40 51 PM" src="https://github.com/user-attachments/assets/23de9b04-a886-4995-b222-681a2efb78b4">

3. Then paste it in the **script** (the highlighted area):

> <img width="916" alt="Screenshot 2024-10-12 at 4 41 45 PM" src="https://github.com/user-attachments/assets/3110ba02-e47a-46d6-83af-301c0103ba6b">

4. Next time you can edit directly there, but I find it better having the script file and editing in an IDE.

---

### Installation

1. Download the `.workflow` file for the Kaomoji Searcher from the repository.
2. Double-click the `.workflow` file to add it to Alfred.
3. You can now search and copy kaomojis using the `k` keyword.
