def main():
    scores = [89,98,75]
    for i in range(3):
        score = int(input('Enter score: '))
        scores.append(score)
    print(score_average(scores))      

def score_average(scores):
    return sum(scores)/len(scores)

main()