:: set PYTHONPATH=%PYTHONPATH%;D:\code\learn\src
:: %~dp0 - This is the folder of THIS script. In this case its expanded to the "bin" folder
set PYTHONPATH=%PYTHONPATH%;%~dp0\..\src
set FOLDER_STUCTURE_PATH=%~dp0\..\resources\config\folder_structure.json
set PROJECTS_INDEX_PATH=%~dp0\..\resources\config\projects_index.json
set OUT=E:\code\learn\resources\publish_test


"C:\Program Files\Side Effects Software\Houdini 17.0.352\bin\houdini.exe" %~dp0\..\scenes\versioning.hip
