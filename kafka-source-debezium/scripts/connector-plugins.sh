if [ $# -ne 1 ]; then
    echo "Usage: connector-plugins.sh \"kafka cluster path\""
else
    curl --location --request GET "$1/connector-plugins"
fi