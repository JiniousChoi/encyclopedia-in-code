# Using Unix Proxy Environment Variable in terminal

export http_proxy=socks5://127.0.0.1:<PORT>
export https_proxy=socks5://127.0.0.1:<PORT>

reference: https://gist.github.com/fearblackcat/850c6e027d5a03017c44daaa6a7ffc30

# How to ping through SOCKS5 proxy?

ICMP protocol won't work over SOCKS, but you can employ nmap to do TCP ping. Check this l4ping to see how to do that.

