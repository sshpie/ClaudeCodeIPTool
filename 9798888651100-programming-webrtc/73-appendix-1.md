# Appendix 1  
Connection Negotiation in Legacy Browsers

Two types of fixes are required to achieve backward compatibility in browsers with older WebRTC implementations. The first type of fix involves manually creating offers and answers—a fix for the very oldest browsers that implement WebRTC. The second type of fix addresses glare. Glare is a state where both peers each have offers out and expect an answer from the other. But neither polite peers on older browsers nor impolite peers on any browser are capable of generating an answer when they have their own offers out. Glare represents a stalemate that cannot be recovered from—unless you step in with a fix yourself.
