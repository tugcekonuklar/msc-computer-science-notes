# Summary

# Risk Assasment

[OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)

* Risk = Likelihood * Impact

Step 1: Identifying a Risk
Step 2: Factors for Estimating Likelihood
Step 3: Factors for Estimating Impact
Step 4: Determining Severity of the Risk
Step 5: Deciding What to Fix
Step 6: Customizing Your Risk Rating Model


## 1) Establishing the context

* Applying the ISO/IEC 27001 Clauses 4 and 5.3 to the company, making any reasonable assumptions that you need to, to
  produce the following:
    * A statement of the purpose of the business
    * A list of internal and external issues that relate to the information security system(s) within the business
    * A list of the interested parties relevant to the information security management system and the
      issues/requirements specific to them
    * A statement of the boundary of the business’s information security system (i.e. where does their ability to
      control and/or responsibility for security end, and what is included inside the boundary?)
    * A list of roles, within the information security management system, and what the responsibilities and authorities
      for those roles are, or should be.

## identfying threats

* BS 7799-3 Clause 6
* “To implement an Information Security Management System (ISMS), ensure compliance with the law, prepare a business
  continuity plan, or meet specific security requirements of our services and/or products.”
    * “ISMS” - an Information Security Management System - clearly identifies the scope as being Information, not
      physical, security.
    * “Compliance with the law” - means we need to think about the laws that apply to the organisation and its
      activities. At a minimum, we’re probably going to have to consider GDPR, but there may be others such as Human
      Rights legislation, financial conduct regulations etc.
    * “Business continuity plan” - a means for keeping the organisation running, albeit at a reduced or minimal level,
      if a disaster happens. That means we need to identify activities within the organisation and prioritise them in
      order of importance to the organisation’s continued survival.
    * “Services and/or products” - again, we need to think about what the organisation does or makes and what the
      security requirements for each of those is.

## 2) Establishing the ISMS boundary

* ISMS boundary - The company is responsible for all systems which it has complete control of, but not responsible for
  any external systems upon which it relies. It will ensure that the data it exchanges with external systems conforms to
  specifications, but cannot reasonably be responsible for the data once it has left the company’s own systems. It will
  share responsibility for data in transit and will only allow data to be transferred in a secure manner.
    * Example:
    * All of the systems that I have listed lie inside the boundary, with the possible exceptions of
        * some customer payment (item c) handling (e.g. customer payments might be outsourced to something like PayPal)
        * HR & payroll (item i) which might be dealt with through an external agency as well
        * Mailing lists (items g and h), which could be outsourced to another third party like Mailchimp
    
    
## 3)  Identifying consequences