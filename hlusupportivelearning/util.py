__author__ = 'luanvu2'
import logging
log=logging.getLogger(__name__)
ERROR={'ExistStudent':'This account already has a student'}
COMMON_ERROR="Have a error !"
class ErrorMessage:
    errors=[]
    def add(self, err):
        if not type(err) is str:
            log.debug("Error Message is not a string object")
            return
        if not err.strip():
            log.debug('Error message is empty')
            return
        err_msg=''
        try:
            err_msg=ERROR[err]
            if err_msg in self.errors:
                return
            self.errors.append(err_msg)
            return
        except:
            pass
        self.errors.append(err)
    def add_err(self, err):
        if not type(err) is str:
            log.debug("Error Message is not a string object")
            return
        if not err.strip():
            log.debug('Error message is empty')
            return
        self.errors.append(err)
    def has_error(self):
        return len(self.errors) > 0
    def list(self):
        return self.errors
