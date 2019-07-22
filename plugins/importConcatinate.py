def FindIn(row, start, end, n=None):
	m = n or len(start)
	RowStart = row.find(start) + m
	RowEnd   = row.find(end, RowStart)
	Result   = row[RowStart:RowEnd]

	return Result


def importConcatinate(src, dist, FileName):
	InFileName = src + FileName 
	OutFileName = dist + FileName 

	FileIn = open(InFileName, 'r')
	Content = FileIn.read()
	FileIn.close()
	ImportCount = str(Content).count('@import url(')
	FileOut = open(OutFileName, 'w')
	FileOut.write(Content)
	FileOut.close()

	for i in range(ImportCount):
		FileOut = open(OutFileName, 'r')
		Content = FileOut.read()
		FileOut.close()

		FileOut = open(OutFileName, 'w')
		FileOut.write(Content)
		FileOut.close()
		ImportFileName = FindIn(Content, "@import url('", "')", 0)
		ImportFileURL = str(src) + ImportFileName

		ImportFile = open(ImportFileURL, 'r')
		ImportFileContent = ImportFile.read()
		ImportFile.close()

		FileOut = open(OutFileName, 'r')
		FileContent = FileOut.read()
		FileOut.close()

		FileOut = open(OutFileName, 'w')
		NewFileContent = str(FileContent).replace("@import url('" + ImportFileName + "')", ImportFileContent)

		FileOut.write(NewFileContent)

	FileOut.close()