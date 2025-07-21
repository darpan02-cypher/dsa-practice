To create a subdirectary in git folder -
mkdir mysubfolder
echo "Hello World" > mysubfolder/hello.txt  // as Git doesn’t track empty folders, so you must add at least one file.
git add mysubfolder
git commit -m "Added mysubfolder with hello.txt"
// To remove a subdirectory, you can use the following command:
git rm -r mysubfolder
