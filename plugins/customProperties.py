def FindIn(row, start, end, n=None):
	m = n or len(start)
	RowStart = row.find(start) + m
	RowEnd   = row.find(end, RowStart)
	Result   = row[RowStart:RowEnd]

	return Result

def customProperties(src, dist, FileName):
	InFileName = src + FileName
	OutFileName = dist + FileName

	FileIn = open(InFileName, 'r')
	Content = FileIn.read()
	FileIn.close()
	VariablesCount = Content.count('--') - Content.count('var(--')

	FileOut = open(OutFileName, 'w')
	FileOut.write(Content)
	FileOut.close()

	for i in range(VariablesCount):
		FileOut = open(OutFileName, 'r')
		FileContent = FileOut.read()
		FileOut.close()

		FileOut = open(OutFileName, 'w')

		Variables = FindIn(FileContent,':root {', '}')
		Variable = FindIn(Variables,'--', ';', 0) + ';'

		VariableName   = FindIn(Variables,'--', ':', 2)
		VariableValue  = FindIn(Variables,VariableName, ';', len(VariableName) + 2)

		ChangeFileContent = str(FileContent).replace('--' +Variable, '')

		NewFileContent = str(ChangeFileContent).replace('var(--' + VariableName +')', VariableValue)

		FileOut.write(NewFileContent)
		FileOut.close()

	FileOut = open(OutFileName, 'r')
	FileContent = FileOut.read()
	FileOut.close()

	Variables = FindIn(FileContent,':root {', '}')

	FileOut = open(OutFileName, 'w')
	FileOut.write(str(FileContent).replace(':root {' + Variables + '}', '/* Created by DelFy */'))

	FileOut.close()