echo "Nomad: Create test job samples"
/usr/bin/nomad init
/usr/bin/nomad run -output example.nomad > example.json
cp example.nomad vault.hcl
sed -i s/"# vault {"/"vault { policies = [\"policy-demo\"]}"/g vault.hcl
sed -i s/"job \"example\" {"/"job \"vault\" {"/g vault.hcl
/usr/bin/nomad run -output vault.hcl > vault.json

