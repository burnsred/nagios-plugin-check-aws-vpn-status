# nagios-plugin-check-aws-vpn-status

All arguments are required:

    usage: check-aws-vpn-status [-h]
                                --region REGION
                                --vpn-connection-id VPN_CONNECTION_ID_1
                                [--aws-access-key-id AWS_ACCESS_KEY_ID]
                                [--aws-secret-access-key AWS_SECRET_ACCESS_KEY]
                                [--vpn-connection-id VPN_CONNECTION_ID_2]
                                [--strict-checking]

Will return 0 (OK) if all VPN connections listed have at least one tunnel up,
and 2 (CRITICAL) otherwise. If you enable ``--strict-checking``, the check will
return 1 (WARNING) if not all possible VPN tunnels are up.
