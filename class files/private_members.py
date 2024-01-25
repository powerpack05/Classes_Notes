# Class : Class is a blueprint for creating new objects
# Object : Instance of the class

class TagCloud:

    def __init__(self):
        self.____tags = {}


    def add(self,tag):
        self.____tags[tag.lower()] = self.____tags.get(tag.lower(),0) + 1


    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(),0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.____tags)

    def __iter__(self):
        return iter(self.__tags)

    def __str__(self):
        return str(self.__tags)

cloud = TagCloud()
print(cloud.__dict__)
cloud.add("python")
cloud.add("Python")
cloud.add("PYTHON")
print(cloud.__tags)
cloud.add("Name")
cloud.add("id")
cloud.add("ID")
print(cloud.__tags)
print(cloud["python"])
print(cloud.__tags['name'])
print(type(cloud))
cloud["python"] = 10
print(cloud.__tags)
print(len(cloud))
for item in cloud:
    print(item)
print(cloud.__tags["PYTHON"])
