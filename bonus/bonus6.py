contents = ['All carrots are to be diced', 
            'The carrots are to be sliced', 
            'Slicing and dicing was done using a knife']

filenames = ['doc.txt', 'reports.txt', 'presentation.txt']

for content,filename in zip(contents, filenames):
    file = open(f'files/{filename}', 'w')
    file.write(content)
    