

echo "Vault: stoping"
PID=`ps -eaf | grep "vault server -dev" | grep -v grep | awk '{print $2}'`
if [ "" !=  "$PID" ]; then
  echo "killing $PID"
  kill -9 $PID
fi

echo "Nomas: stoping"
PID=`ps -eaf | grep "nomad agent -server" | grep -v grep | awk '{print $2}'`
if [ "" !=  "$PID" ]; then
  echo "killing $PID"
  kill -9 $PID
fi

rm -rf example.json example.nomad
