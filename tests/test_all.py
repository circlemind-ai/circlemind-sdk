from circlemind import Circlemind

if __name__ == '__main__':
    cm = Circlemind("YOUR_API_KEY", "http://ec2-3-81-205-157.compute-1.amazonaws.com")

    memories = cm.get_memories("What animals do I like?")
    
    print(memories)
