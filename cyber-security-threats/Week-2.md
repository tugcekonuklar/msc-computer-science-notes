#### Main Topics

* Identify human and human-related factors which adversely affect cyber security (MLO 1)
* Identify and explain the significance and effect of common flaws in some common human interface elements (MLO 1, 4, 5)
* Demonstrate understanding of the importance of input check and sanitisation as a security mechanism (MLO 4, 5).

#### Sub titles:

# Human factors

* Information in computers are intangible, tahts why hard to understand humans the importance.
* Even they know the value of the data stored in it, they cause several breaches on the securities, like disclosing
  passwords, leaving laptops open etc.
* Even they aware of the potential securoty issues, hackers try to manipulate them with various technical or
  psychological ways.

## The Web—User Side

* Security issues for browsers arise from several complications to that simple description, such as these:
    * A browser often connects to more than the one address shown in the browser’s address bar.
    * Fetching data can entail accesses to numerous locations to obtain pictures, audio content, and other linked
      content.
    * Browser software can be malicious or can be corrupted to acquire malicious functionality.
    * Popular browsers support add-ins, extra code to add new features to the browser, but these add-ins themselves can
      include corrupting code.
    * Data display involves a rich command set that controls rendering, positioning, motion, layering, and even
      invisibility.
    * The browser can access any data on a user’s computer (subject to access control restrictions); generally the
      browser runs with the same privileges as the user.
    * Data transfers to and from the user are invisible, meaning they occur without the user’s knowledge or explicit
      permission.
* Browsers connect users to outside networks, but few users can monitor the actual data transmitted
* A browser’s effect is immediate and transitory: pressing a key or clicking a link sends a signal, and there is seldom
  a complete log to show what a browser communicated. In short, browsers are standard, straightforward pieces of
  software that expose users to significantly greater security threats than most other kinds of software

### Browser Attacks

* There are three attack vectors against a browser:
    * Go after the operating system so it will impede the browser’s correct and secure functioning.
    * Tackle the browser or one of its components, add-ons, or plug-ins so its activity is altered.
    * Intercept or modify communication to or from the browser.

* **Man-in-the-Browser:**
    * A man-in-the-browser attack is an example of malicious code that has infected a browser. Code inserted into the
      browser can read, copy, and redistribute anything the user enters in a browser. The threat here is that the
      attacker will intercept and reuse credentials to access financial accounts and other sensitive data.
    * Man-in-the-browser: Trojan horse that intercepts data passing through the browser
      <img src="./img/2/1.png" alt="alt text" width="500" height="300"></br>
* **Keystroke Logger**
    * A keystroke logger (or key logger) is either hardware or software that records all keystrokes entered.
    * The logger either retains these keystrokes for future use by the attacker or sends them to the attacker across a
      network connection.

* Page-in-the-Middle
    * A page-in-the-middle attack is another type of browser attack in which a user is redirected to another page.
      Similar to the man-in-the-browser attack, a page attack might wait until a user has gone to a particular web site
      and present a fictitious page for the user.
        * As an example, when the user clicks “login” to go to the login page of any site, the attack might redirect the
          user to the attacker’s page, where the attacker can also capture the user’s credentials.
* **Program Download Substitution**
    * Coupled with a page-in-the-middle attack is a download substitution.
    * In a download substitution, the attacker presents a page with a desirable and seemingly innocuous program for the
      user to download, for example, a browser toolbar or a photo organizer utility.
    * What the user does not know is that instead of or in addition to the intended program, the attacker downloads and
      installs malicious code.
    * A user agreeing to install a program has no way to know what that program will actually do.
* **User-in-the-Middle**
    * A different form of attack puts a human between two automated processes so that the human unwittingly helps
      spammers register automatically for free email accounts.
    * A CAPTCHA is a puzzle that supposedly only a human can solve, so a server application can distinguish between a
      human who makes a request and an automated program generating the same request repeatedly.
    * CAPTCHA -> Completely Automated Public Turing test to tell Computers and Humans Apart
    * How captcha vulneribility can be eliminated?
        * By introducing some degree of randomness, such as an unpredictable number of characters in a string of text.

### Authentication

* The central failure of these in-the-middle attacks is faulty authentication.
* If A cannot be assured that the sender of a message is really B, A cannot trust the authenticity of anything in the
  message.
* **Human Authentication**
    * face-to-face authentication.
    * human-to-computer authentication that used sophisticated techniques such as biometrics and so-called smart
      identity cards.
    * These human factors can affect authentication in many contexts because humans often have a role in authentication,
      even of one computer to another.
* **Computer Authentication**
    * Computer authentication uses the same three primitives as human authentication, with obvious variations.
    * The problem, such as cryptographic key exchange, is how to develop a secret shared by only two computers.
    * In addition to obtaining solid authentication data, you must also consider how authentication is implemented.
    * if software can interfere with the authentication-checking code to make any value succeed, authentication is
      compromised. Thus, vulnerabilities in authentication include not just the authentication data but also the
      processes used to implement authentication.
    * Authentication discussion two-sided issue: The system needs assurance that the user is authentic, but the user
      needs that same assurance about the system.
        * This second issue has led to a new class of computer fraud called **phishing**, in which an unsuspecting user
          submits sensitive information to a malicious system impersonating a trustworthy one.
        * Common targets of **phishing** attacks are banks and other financial institutions: Fraudsters use the
          sensitive data they obtain from customers to take customers’ money from the real institutions.
        * Other phishing attacks are used to plant malicious code on the victim’s computer.


* Authentication is vulnerable at several points:
    * Usability and accuracy can conflict for identification and authentication: A more usable system may be less
      accurate. But users demand usability, and at least some system designers pay attention to these user demands.
    * Computer-to-computer interaction allows limited bases for authentication. Computer authentication is mainly based
      on what the computer knows, that is, stored or computable data. But stored data can be located by unauthorized
      processes, and what one computer can compute so can another.
    * Malicious software can undermine authentication by eavesdropping on (intercepting) the authentication data and
      allowing it to be reused later. Well- placed attack code can also wait until a user has completed authentication
      and then interfere with the content of the authenticated session.
    * Each side of a computer interchange needs assurance of the authentic identity of the opposing side. This is true
      for human-to-computer interactions as well as for computer-to-human.

* Successful Identification and Authentication
    * Appealing to everyday human activity gives some useful countermeasures for attacks against identification and
      authentication.
    * **Shared Secret**
        * Banks and credit card companies struggle to find new ways to make sure the holder of a credit card number is
          authentic.
            * For example, mums maiden name
        * financial institutions are asking new customers to file the answers to questions presumably only the right
          person will know
        * The basic concept is of a shared secret, something only the two entities on the end should know
            * To be effective, a shared secret must be something no malicious middle agent can know.
    * **One-Time Password**
        * As its name implies, a one-time password is good for only one use. To use a one-time password scheme, the two
          end parties need to have a shared secret list of passwords.
        * When one password is used, both parties mark the word off the list and use the next word the next time.
    * **Out-of-Band Communication**
        * Out-of-band communication means transferring one fact along a communication path separate from that of another
          fact.
            * For example, bank card PINs are always mailed separately from the bank card so that if the envelope
              containing the card is stolen, the thief cannot use the card without the PIN

    * **Continuous Authentication**
        * If two parties carry on an encrypted communication, an interloper wanting to enter into the communication must
          break the encryption or cause it to be reset with a new key exchange between the interceptor and one end.
        * Both of these attacks are complicated but not impossible.
            * However, this countermeasure is foiled if the attacker can intrude in the communication pre-encryption or
              post-decryption.
        * Encryption can provide continuous authentication, but care must be taken to set it up properly and guard the
          end points.      
    