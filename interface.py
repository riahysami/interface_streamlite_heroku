# Import python packages
import streamlit as st
import requests
import json
url = "https://api.fivetran.com/v1/connectors/{{connector_id}}/sync"
payload = json.dumps({
  "force": False
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic N2N3MzJqQU9kUHdIb3dxajpxTlE2S2VBdjBiaU5DbUtOU2M0MGYwdGlYOHY2WERXaA==',
  'Cookie': 'INGRESSCOOKIE=2228721ad775727b67383997b2575750|bac6da9b4d464a443a3af1340233b03f'
}
#response = requests.request("POST", url, headers=headers, data=payload)
# Write directly to the app
st.title("Run Obi :ballon_gonflable:")
if st.button('Run Boond in DEV'):
    response = requests.request("POST", url, headers=headers, data=payload)
    st.write("response")
else:
    st.write('Too Bad')