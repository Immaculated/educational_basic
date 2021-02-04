class SingleTag:
    
    def __init__(self, name, params):
        self.name = name
        self.params = params
           
    def show(self):
        print('<' + self.name, end=' ')
        for k, v in self.params.items():
            print(f'{k}="{v}"', end=' ')
        print('>')

image = SingleTag('img', dict(src="image.png", width=240))
image.show()