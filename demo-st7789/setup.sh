#
# This BASH script links the required modules in the

## Need to change this to your remote-display path
GITHUB_DIR="NEED"
# example:
# GITHUB_DIR=~/src/github/remote-display
DEMO_DIR=demo-st7789

DISPLAY_MODULES_FILES=(\
    "remote_display.py" \
    "trace_display.py" \
    "dummy_display.py" \
    "st7789py.py" \
    "st7789py_display.py" \
    )
AREA_MODULES_FILES=(\
    "remote_area.py" \
    "remote_7segment.py" \
    "remote_container.py" \
    "remote_image.py" \
    "remote_sysfont.py" \
    "remote_text.py" \
    )
COMM_MODULES_FILES=(\
    )

if [ $GITHUB_DIR = "NEED" ]
then
    echo "GITHUB_DIR path needs to be set (see script example)"
    exit 1
fi

echo "Current directory: $(pwd)"
echo "Source directory: ${GITHUB_DIR}"
echo "Destination directory: ${GITHUB_DIR}/${DEMO_DIR}"

########## display_modules ###########################
directory="display_modules"
for file_name in "${DISPLAY_MODULES_FILES[@]}"
do
    echo "DISPLAY: $file_name"
    ln -sf ${GITHUB_DIR}/${directory}/${file_name} \
        ${GITHUB_DIR}/${DEMO_DIR}/${directory}/${file_name}
done

########## area_modules ###########################
directory="area_modules"
for file_name in "${AREA_MODULES_FILES[@]}"
do
    echo "AREA: $file_name"
    ln -sf ${GITHUB_DIR}/${directory}/${file_name} \
        ${GITHUB_DIR}/${DEMO_DIR}/${directory}/${file_name}
done

########## comm_modules ###########################
directory="comm_modules"
echo "COMM: Not needed for ${DEMO_DIR}"

# That's All Folks


