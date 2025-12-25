# placeholder
class Store < ApplicationRecord
  has_many :question_logs

  validates :shop_domain, presence: true, uniqueness: true
  validates :access_token, presence: true
end
