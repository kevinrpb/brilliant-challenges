# use as `./new.sh "title"`

YEAR=`date +%Y`
DATE=`date +%Y-%m-%d`
TITLE=$1
TITLE=${TITLE// /-}


if [ ! -d "$YEAR" ]; then
	mkdir $YEAR
fi

TEMP="template"
FILE="$YEAR/$DATE-$TITLE.md"

# Check if file already exists
if [ ! -f $FILE ]; then
	# Copy it
	cp $TEMP $FILE

	# Check if it was copied
	if [ -f $FILE ]; then
		echo "Created file $FILE"

		# Replace date and title
		sed -i -e "s/YYYY-MM-DD/$DATE/g" $FILE
		sed -i -e "s/TITLE/$1/g" $FILE

		# Delete sed file
		rm "$FILE-e"
	else
		echo "Error creating file $FILE"
	fi
else
	echo "File $FILE already exists"
fi
