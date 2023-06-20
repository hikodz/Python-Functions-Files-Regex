file_path = {
'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/atomic_habits_summary.txt': r'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/atomic_habits_summary_edit.txt',
'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/deep_work_summary.txt': r'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/deep_work_summary_edit.txt', 
'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/dopamine_nation_summary.txt': r'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/dopamine_nation_summary_edit.txt'
}
def custom_book(file_path):
    for path, new_path in file_path.items():
        with open(path) as real, open(new_path, 'w') as fake:
            read_book = real.readlines()
            edit_book = [fake.write(f'{line[::-1].strip().upper()}\n') for line in read_book]
custom_book(file_path)
#####################################################
import os
books_list = [
    "atomic_habits_summary",
    "so_good_to_ignore_summary",
    "dopamine_nation_summary",
    "deep_work_summary",
    "the_lady_tasting_tea_summary",
    "the_power_of_habits_summary"
]

def creat_summaries(books_list):
    
    output_folder = "/Users/mohamedbloul/Desktop/codzilla cours/Section 12/books_summaries"
    os.makedirs(output_folder, exist_ok=True)
    
    for book in books_list:
        
        path_one = f'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/{book}.txt'
        path_two = f'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/books_summaries/books_summaries.txt'
        path_thr = f'/Users/mohamedbloul/Desktop/codzilla cours/Section 12/books_summaries/{book}.txt'
        
        with open(path_one) as before, open(path_two, "a") as after, open(path_thr, "w") as add:
            file_summaries = before.read()
            add.write(file_summaries)
            after.write(f"\n-->{book.replace('_', ' ').title()}:\n{file_summaries}\n")

creat_summaries(books_list)

