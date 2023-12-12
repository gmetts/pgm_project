CURR_DIR="$(pwd)"
FILE_PATH="$CURR_DIR/$1"
cd ~/.local/share/ov/pkg/isaac_sim-2023.1.0-hotfix.1
echo "$FILE_PATH"
./python.sh "$FILE_PATH"