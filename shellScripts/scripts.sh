#!/bin/bash
#El primer parámetro determina la función a llamar, el segundo, el parámetro que debe recibir la función

isInstalledAndWhere()
{
    locate share/torbrowse > aux
    if [[ "$2" = "inst" ]]; then
        echo "ENTRO"
        wc -l aux
    else
        echo "NO ENTRO"
        head -1 aux
    fi
    rm -rf aux
}

if [ -z "$2" ]; then echo "var is unset"
fi

if [[ $(($1)) == 1 ]]
then
    isInstalledAndWhere
else
    echo "HOLA WEYS WEYS"
fi
