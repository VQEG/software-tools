# Disable SSL verification for local Jekyll development
require 'net/http'
require 'openssl'

module Net
  class HTTP
    alias_method :original_start, :start

    def start(&block)
      if use_ssl?
        self.verify_mode = OpenSSL::SSL::VERIFY_NONE
      end
      original_start(&block)
    end
  end
end
