from classes.Homework import Homework

homework = Homework()
homework.get_book()

# Sequencial
homework.run_sequencial_test(30)

# 2 Threads
homework.run_paralell_test(2, 30)

# 4 Threads
homework.run_paralell_test(4, 30)

# 8 Threads
homework.run_paralell_test(8, 30)

# Stopup
homework.compare_results()