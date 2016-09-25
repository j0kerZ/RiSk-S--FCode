# SAP - A toolkit that protect many email security issues for your company base

SAP is a SMTP inspectable proxy comes with advance malware/phising detection with yara and data leakage prevention with text mining


#Usage:
 SAP_proxy.py [-h] [--bind_address BIND_ADDRESS]
                     [--bind_port BIND_PORT] [--remote_address REMOTE_ADDRESS]
                     [--remote_port REMOTE_PORT]
                     [--base_log_directory BASE_LOG_DIRECTORY]
                     [--log_all_messages] [--block] [--always_block]
                     [--save_attachments] [--log_config LOG_CONFIG]
                     --processor PROCESSORS [PROCESSORS ...]

optional arguments:
  -h, --help            show this help message and exit
  --bind_address BIND_ADDRESS
                        Address to bind to and listen on for incoming mail.
                        Default is 127.0.0.1
  --bind_port BIND_PORT
                        Port to bind to and to listen on for incoming mail.
                        Default is 1025
  --remote_address REMOTE_ADDRESS
                        Remote address to forward outbound mail. Default is
                        127.0.0.1
  --remote_port REMOTE_PORT
                        Remote port to forward outbound mail. Default is 25
  --base_log_directory BASE_LOG_DIRECTORY
                        Directory to write log files, messages, and
                        attachments. Default is /usr/local/SAP/
  --log_all_messages    Log all messages to /base_log_directory/messages/
  --block               Block mail with quarantined attachments. Default is
                        False
  --always_block        Turn the proxy into a server (block all). Default is
                        false
  --save_attachments    Experimental: Save all attachments as seperate files.
                        Default is false.
  --log_config LOG_CONFIG
                        Logging config file. Default is /etc/SAP/logging.conf

required:
  --processor PROCESSORS [PROCESSORS ...]
                        Choose a processing engine by supplying an import
                        string as the first positional argument and multiple
                        rules files as optional following arguments. For
                        example: --processor SAP.processors.yara_processor
                        /etc/SAP/rules/malware_pdf
```

#Example

python sap_proxy --block --processor SAP.processors.yara_processor rules/malware_pdf rules/scam


#Dependencies
SAP is heavily based on: 
Bulk
Yara

# Contributing
We love to hear from people using our tools and code.
Feel free to discuss issues on our issue tracker and make pull requests!
