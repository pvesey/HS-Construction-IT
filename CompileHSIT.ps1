$Assignment1 = [PSCustomObject]@{
    Name = 'HSIT01-LIT-00-ZZ-SP-A-001-A1-P01'
    Spec = './Assignments/HSIT01-LIT-00-ZZ-SP-A-001-A1-P01.tex'
    HomeDir = './HSIT01/'
    Archive = 'HSIT01-LIT-00-ZZ-IE-A-001-A1-P01.zip'
}

$Assignment2 = [PSCustomObject]@{
    Name = 'HSIT02-LIT-00-ZZ-SP-A-001-A1-P01'
    Spec = './Assignments/HSIT02-LIT-00-ZZ-SP-A-001-A1-P01.tex'
    HomeDir = './HSIT02/'
    Archive = 'HSIT02-LIT-00-ZZ-IE-A-001-A1-P01.zip'
}

$Assignment3 = [PSCustomObject]@{
    Name = 'HSIT03-LIT-00-ZZ-SP-A-001-A1-P01'
    Spec = './Assignments/HSIT03-LIT-00-ZZ-SP-A-001-A1-P01.tex'
    HomeDir = './HSIT03/'
    Archive = 'HSIT03-LIT-00-ZZ-IE-A-001-A1-P01.zip'
}

$AssetLocation = './Assets/'
$Sheet = 'LIT-A1-Metric-Arch.rfa'

# Cleanout folders
Remove-Item ($Assignment1.HomeDir + '*.*')
Remove-Item ($Assignment2.HomeDir + '*.*')
Remove-Item ($Assignment3.HomeDir + '*.*')
Write-Host 'HomeDir Cleanout'

# Copy Items to Pack Folders

#Copy-Item ($AssetLocation + $Sheet) ($Assignment1.HomeDir + $Sheet) -Force
#Copy-Item ($AssetLocation + $Sheet) ($Assignment2.HomeDir + $Sheet) -Force
#Copy-Item ($AssetLocation + $Sheet) ($Assignment3.HomeDir + $Sheet) -Force
#Copy-Item ($AssetLocation + $Sheet) ($Assignment4.HomeDir + $Sheet) -Force
#Write-Host 'A1 Sheet Copied to Packs'

# Compile Latex Files


pdflatex $Assignment1.Spec
Remove-Item ($Assignment1.Name + '.aux')
Remove-Item ($Assignment1.Name + '.log')
Remove-Item ($Assignment1.Name + '.out')
Move-Item -Path ($Assignment1.Name + '.pdf') -Destination ($Assignment1.HomeDir + $Assignment1.Name + '.pdf') -Force

pdflatex $Assignment2.Spec
Remove-Item ($Assignment2.Name + '.aux')
Remove-Item ($Assignment2.Name + '.log')
Remove-Item ($Assignment2.Name + '.out')
Move-Item -Path ($Assignment2.Name + '.pdf') -Destination ($Assignment2.HomeDir + $Assignment2.Name + '.pdf') -Force


#pdflatex $Assignment3.Spec
#Remove-Item ($Assignment3.Name + '.aux')
#Remove-Item ($Assignment3.Name + '.log')
#Remove-Item ($Assignment3.Name + '.out')
#Move-Item -Path ($Assignment3.Name + '.pdf') -Destination ($Assignment3.HomeDir + $Assignment3.Name + '.pdf') -Force


Remove-Item $Assignment1.Archive
Remove-Item $Assignment2.Archive
#Remove-Item $Assignment3.Archive


Compress-Archive $Assignment1.HomeDir $Assignment1.Archive -Update
Compress-Archive $Assignment2.HomeDir $Assignment2.Archive -Update
#Compress-Archive $Assignment3.HomeDir $Assignment3.Archive -Update



Write-Host -NoNewLine 'Script Complete: Press any key to continue...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');