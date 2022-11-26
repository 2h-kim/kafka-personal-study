if [ $# -ne 2 ]; then
    echo "Usage: connector-plugins.sh $0 \"kafka cluster path\" \"configure path\""
else
    curl --location --request POST "$1/connectors" \
        --header 'Content-Type: application/json' \
        -d @$2
fi