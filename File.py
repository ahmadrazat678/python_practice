def generatetables(n):
    tale = ""
    for i in range(1,11):
        table+=f"{n} x {i} = {n*i}\n"

    with open(f"tables/tale_{n}", "w") as f:
        f.write(table)