n=$1
for file in *.dat; do
	cp "$file" "${file}_$n"
done
