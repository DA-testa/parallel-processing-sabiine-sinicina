# python3

def parallel_processing(n, m, data):
    output = []
    processors = [(0, i) for i in range(n)]
    for task in data:
        next_processor = min(processors)[1]
        output.append((next_processor, processors[next_processor][0]))
        processors[next_processor] = (processors[next_processor][0] + task, next_processor)
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))


    result = parallel_processing(n,m,data)
    
    for thread, time in result:
        print(thread, time)



if __name__ == "__main__":
    main()
