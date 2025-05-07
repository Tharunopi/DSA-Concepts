class Looper:
    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end

    def __enter__(self):
        print("Loop initiated...")
        values = []
        for i in range(self.end):
            print(i)
            values.append(i)

        return values
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Loop Exited!.")
        
with Looper() as l:
    print("ok")