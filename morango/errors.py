class MorangoError(Exception):
    pass


class ModelRegistryNotReady(MorangoError):
    pass


class InvalidMorangoModelConfiguration(MorangoError):
    pass


class UnsupportedFieldType(MorangoError):
    pass


class MorangoCertificateError(MorangoError):
    pass


class CertificateScopeNotSubset(MorangoCertificateError):
    pass


class CertificateSignatureInvalid(MorangoCertificateError):
    pass


class CertificateIDInvalid(MorangoCertificateError):
    pass


class CertificateProfileInvalid(MorangoCertificateError):
    pass


class CertificateRootScopeInvalid(MorangoCertificateError):
    pass


class MorangoNonceError(MorangoError):
    pass


class NonceDoesNotExist(MorangoNonceError):
    pass


class NonceExpired(MorangoNonceError):
    pass


class MorangoServerDoesNotAllowNewCertPush(MorangoError):
    pass


class MorangoResumeSyncError(MorangoError):
    pass


class MorangoContextUpdateError(MorangoError):
    pass


class MorangoLimitExceeded(MorangoError):
    pass


class InvalidMorangoSourceId(MorangoError):
    pass


class MorangoInvalidFSICPartition(MorangoError):
    pass


class MorangoSkipOperation(MorangoError):
    pass
