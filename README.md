# nagios-plugin-check-aws-vpn-status

All arguments are required:

    usage: check-aws-vpn-status [-h]
                                --aws-access-key-id AWS_ACCESS_KEY_ID
                                --aws-secret-access-key AWS_SECRET_ACCESS_KEY
                                --region REGION
                                --vpn-connection-id VPN_CONNECTION_ID_1
                                [--vpn-connection-id VPN_CONNECTION_ID_2]

Will return 0 (OK) if all VPN connections listed have at least one tunnel up,
and 1 (CRITICAL) otherwise.