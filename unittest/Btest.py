from requests import Request,session

s = session()
req = Request('GET', url,
    data=data,
    headers=headers
)

# prepped = req.prepare()
prepped = s.prepare_request(req)

resp =  s.send(prepped,
               stream=stream,
               verify=verify,
               proxies=proxies,
               cert=cert,
               timeout=timeout
               )

print(resp.status_code)