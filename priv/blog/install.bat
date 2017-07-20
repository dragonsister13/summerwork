REM Run this script to automatically install or reinstall all packages,
REM as it's performed by the Unity Download Assistant.
REM Needs to be run with superuser permissions.

"UnitySetup64.exe" -UI=reduced /D=C:\Program Files\Unity
"UnityDocumentationSetup.exe" /S /D=C:\Program Files\Unity
"UnityStandardAssetsSetup.exe" /S /D=C:\Program Files\Unity
"vs_Community.exe" --productId "Microsoft.VisualStudio.Product.Community" --add "Microsoft.VisualStudio.Workload.ManagedGame" --campaign "Unity3d_Unity" --passive --norestart
