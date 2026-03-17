param(
    [Parameter(Mandatory = $true)]
    [string]$DisplayName,

    [Parameter(Mandatory = $true)]
    [string]$UserPrincipalName,

    [string]$JobTitle,
    [string]$Department,
    [string]$TemporaryPassword = "Alterar123!"
)

# Template base para criação de usuários no Microsoft Entra ID.
# Revisar naming convention, domínio, atributos obrigatórios, licença e grupos antes do uso em produção.

$mailNickname = ($UserPrincipalName -split '@')[0]

New-MgUser `
  -DisplayName $DisplayName `
  -UserPrincipalName $UserPrincipalName `
  -JobTitle $JobTitle `
  -Department $Department `
  -MailNickname $mailNickname `
  -AccountEnabled:$true `
  -PasswordProfile @{
      Password = $TemporaryPassword
      ForceChangePasswordNextSignIn = $true
  }
