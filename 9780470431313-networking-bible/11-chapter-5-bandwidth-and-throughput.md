# Chapter 5. Bandwidth and Throughput

**IN THIS CHAPTER**

- Learn how signals are used to send data
- See how to store and recreate complex data
- Learn how multiple data streams can share the same connection
- Understand resource allocation and traffic control methods

Information flows over a network as a series of signals. Those signals can represent either analog or digital data. Groups of signals are defined by various standards to represent different types of data. Some groups can be character sets, and some groups might be the various notes of a song or words in a conversation. It is up to various protocols to encode and decode the data, while other protocols are responsible for transporting and controlling the flow of the data. A collection of data represents information. The bandwidth of a network segment, its throughput, and its capacity are described.

Signals that carry data are transferred in the form of periodic waves. Any periodic function or complex waveform can be described by a Fourier transform, which is a mathematical operation that takes a complex waveform and transforms it into another set of simpler sinusoidal functions and coefficients. This analysis creates a set of terms called *harmonics* that perform curve fitting. This process is needed to store information and recreate it later.

A waveform can be recreated by sampling the wave and splitting it into small components. Sampling theory places a limit on the amount of sampling you can do and still obtain useful information.

Multiple streams of data can be sent over the same network connection using a technique called *multiplexing*. There are many different forms of multiplexing. Some use time division, others frequency division, and a few use polarization division to separate one data stream from another. Multiplexing must be supported by protocols and is responsible for one network type being different from another.

Higher-level protocols are used to control the flow of traffic over a network. For IP networks, this is called *packet shaping*. Traffic control can look at data types, destination, and other factors and change the priority with which data is sent, limit the bandwidth, and perform other actions. The collection of technologies that assign network traffic to network resources is called *Quality of Service* (QoS).

# Bandwidth and Capacity

Information is transmitted through a medium such as copper metal in an Ethernet wire by the flow of electrons past a point. The signal is carried by the manner in which the current, the voltage, the frequency, or the phase, or some combination thereof changes periodically with time. It is the variation in the amplitude and/or the frequency of the current that is most often used to turn a signal into data.

The signals that flow over a wire are analog signals, even when they encode for digital signals. A system can send a near perfect square wave for a 1-bit value, but noise, signal contention, and many other factors degrade the signal. The receiving system must measure the signals for their periodicity and for the range of values that the bit falls into to determine whether it represents 1 bit.

Computer networks can use different media to transmit data from point to point. Optical wires transmit light as the signal carrier, Bluetooth and Wi-Fi use radio frequency waves, WIMAX uses microwaves, and so on. The description of the signals is different, but the ideas of bandwidth, throughput, capacity, and other concepts described in this chapter are similar.

## Beads flow through a pipe of syrup

The Zen master asks you to close your eyes, take a deep breath, and visualize, if you will, beads flowing through a pipe filled with syrup floating in front of you. (This is the networking equivalent of a Lava lamp.)

Every networked medium has limiting factors that place a ceiling on the bandwidth and capacity of the data flow. If you think of a network connection as a pipe that is filled with some medium (syrup, perhaps) through which some particle or wave flows (the beads), then you can measure the flow of the beads in several important ways that can be used to transmit data that can be interpreted as information. A bead doesn't have enough of a wavelength that it can be measured, but Heisenberg's uncertainty principle defines what that wavelength is.

The diameter of the pipe determines the maximum number of beads that can flow past any point at any one time: that is the bandwidth. The pressure of beads applied affects the speed of the beads up to some maximum level above which the technology that you push with can't go faster. The pressure corresponds to the potential energy you are applying; in a wire, pressure corresponds to voltage. The speed of the flowing beads past any given point gives rise to the observation of a flux, which is the amount of beads per unit time. The flux defines the throughput. The corresponding throughput in a wire is the current, which is the number of electrons that pass a point per unit of time.

Taken together, the maximum bandwidth and throughput represent the amount of beads that the pipe of syrup can carry, which is the capacity of the pipe. Some capacities are practical; the method used to apply pressure just can't go any higher. Other capacities are theoretical; the pipe bursts. Electrically that is equivalent to current flowing through a wire or a transistor creating a defect such as electromigration that destroys the wire or the junction of the transistor that forms a switch. Electromigration results in a hole in the wire as the metal itself moves with the current.

Because a collection of beads represents information, your data rate corresponds directly with the rate at which the beads flow. The rate of beads depends on the bandwidth of the pipe that feeds the flow. Speeds and feeds are fundamental performance metrics that you use to measure the efficiency of any data network.

These are simple concepts, but they apply to any network segment. The different factors determine what you can do on a network, how much data can be carried, when there is too much data for the medium to carry, and so on. There isn't enough room to cover all of the physics you need to know in relation to electricity, optics, and radiotelegraphy (radio messenger), but a simple example of signal theory can help you better appreciate the concepts that follow.

## Signaling

Let's say that you have an electric current traveling down a wire over a certain period of time that you want to use to communicate with. The message is a short one: Save Our Ship, which is transmitted using the acronym S-O-S. You encode the message in Morse code, which means that it consists of three short signals for the letter S (dots) and three long signals for the letter O (dash).

Encoding a dot corresponds to a signal of 1 (On) for one time period. A dash is a signal of 1 (On) for two consecutive time periods. A signal that is On corresponds to an amplitude between a certain range of values, while an Off signal has an amplitude of between zero and the start of the On range. [Figure 5.1](ch05.html#an_idealized_sos_digital_signal) shows the digital SOS signal that you've just constructed. In the real world, signals aren't perfect square waves and there are certain variations in the shape of each signal that are tolerated.

[Figure 5.1](ch05.html#an_idealized_sos_digital_signal) is meant to illustrate some of the complexities of electrical signal. The signal is carried over the time domain, with a periodicity of 8 measured amplitudes (voltage) per cycle. If a time period has an amplitude in the 1 range, it is considered to be ON, and if the amplitude is in the 0 range, it is considered to be OFF. That is the reason why the first S looks different than the second S, but is interpreted as the same data.

![An idealized SOS digital signal](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0501.png)

**Figure 5.1. An idealized SOS digital signal**

It's easy to represent our SOS as a pictograph, but what if you wanted to be able to mathematically describe the signal so that you could re-create it if you needed to. When Sir Isaac Newton wanted to calculate the area under a curve, he developed calculus to create rectangular slices that he could calculate. The finer the slice, the closer the calculated sum is to the real area. This analysis is called *integration*, and the mathematical representation used is an *integral*.

For a signal with an imposed periodicity (frequency), the problem is somewhat different. You still want to approach the problem by breaking the overall shape into smaller shapes that you can calculate, but here you need periodic time varying function(s) to do so. This is exactly the problem that Joseph Fourier faced when he tried to analyze heat flow. His solution was to break the signal into a large set of increasingly more precise trigonometric functions.

The process by which the signal is broken apart is called a *Fourier analysis*, the equations that describe the result are a *Fourier transform*, and the process by which the signal can be reconstructed is called *Fourier synthesis*. For data signals of the type you are considering here, the functions used are typically the sine and cosine functions.

The general form of a 2π periodic Fourier function is:

**Equation 5.1.**

![An idealized SOS digital signal](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/U0501.png)

where the frequency f is 1/T, and an and bn are the amplitudes of the nth harmonics. A harmonic of a wave is the frequency of the signal divided by an integer so that the resulting function still retains the same periodicity. The equation above leads to a series of terms based on the value of n. The more terms used in a Fourier series, the closer the curve fits the signal that you are trying to represent. The equation above can be manipulated so that you can solve for the constants for each term you use: an, bn, and so forth individually, but the details are not important for this discussion.

The result of applying multiple harmonics to fit a square wave is shown in [Figure 5.2](ch05.html#a_fourier_transform_curve_fitting_to_a_s). The square wave is f(t), and the other two curves approximate the square wave. The coarser curve is the fifth harmonic k = 5, and the finer curve is the fifteenth harmonic k = 15.

![A Fourier transform curve fitting to a step function for a fifth and fifteenth harmonic](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0502.png)

**Figure 5.2. A Fourier transform curve fitting to a step function for a fifth and fifteenth harmonic**

Although the example shown is just one square wave, Fourier analysis can create a representation for a collection of square waves, ramps, or sawtooths, or any other time varying function. You can run a complex audio signal through a Fourier analysis and derive a formula that describes it, or apply Fourier analysis to a spectrum.

How does this all relate to our SOS signal? The frequency of the signal is the number of cycles per unit time that passes a point in time, that is, f = 1/T. A computer has no way to determine where one cycle begins and another cycle ends, but the computer does have a clock. Data is sent so that each character is represented by a standard bit length value, called a *byte*.

Last time I checked, computers weren't using Morse code; what they do use is one of many character sets based on published standards. One standard is 7-bit ASCII, which can vary by locale; another standard is Unicode. For American and British ASCII character sets, the bit pattern for an S is 1010011, while the bit pattern for an O is 1000011. If your computer communicates in 8-bit bytes, then the signal is padded with zeros so it reaches the required length. In 8-bit representation, S is 01010011 and O is 01000011 — note one zero is padded at the beginning of each 7-bit sequence to make them 8 bits. A Fourier series can define these bytes in the correct sequence. In [Figure 5.2](ch05.html#a_fourier_transform_curve_fitting_to_a_s), the byte is 8 bits long, adding extra zeros to the S bits in order to bring them up to the length of the O byte.

A system that uses the amplitude of a signal to encode data is referred to as *amplitude modulation*. In the radio frequency world, AM is the basis for talk radio. Another method for encoding data is *frequency modulation*. Frequency modulation in the radio frequency world gives us FM and NPR. The third method used to encode data is called *phase modulation*. You use a change in the signal's phase to switch a signal on or off. The phase of a wave is the amount of a wave's offset from a reference time.

[Figure 5.3](ch05.html#amplitude_comma_frequency_comma_and_phas) shows an example of these three different modulation techniques and how they are used to encode data by altering the carrier wave. The first figure for amplitude modulation shows a signal is contained in the amplitude of the wave. As you move left to right, the first maximum would represent a 1 or ON signal, and the minimum part of the wave on the right would be a 0 or OFF signal. As the wave moves off the right hand portion of the figure, it is rising, perhaps indicating that another 1 is next. However, the wave could just as well continue with the low amplitude signal. Amplitude measurements in an amplitude modulation scheme are measured at timed intervals.

The middle figure for frequency modulation shows a set of transitions which are from left to right: low frequency, high frequency, low frequency, and finally high frequency. As measured periodically this usually represents the pattern: 0, 1, 0, and 1.

Phase modulation is a little more subtle. In the bottom figure you see two transitions resulting in three different waveforms. The middle waveform is phase modulated, that is offset from the other two waveforms. The transitions of the phases encode the signals that are translated into data.

![Amplitude, frequency, and phase modulation can all encode data.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0503.png)

**Figure 5.3. Amplitude, frequency, and phase modulation can all encode data.**

## Bandwidth

Bandwidth is a term that can have one of several related meanings. In digital communications the bandwidth of any channel, connection, link, or pipe is the amount of data that may be transferred per unit time. This type of bandwidth measures capacity and is sometimes referred to as the available bandwidth. Bandwidth can also measure throughput, which is stated in terms of available bandwidth or capacity.

In terms of the discussion in this chapter, the bandwidth we are interested in describes the frequency range of signals that are allowed to pass over a circuit usually in terms of cycles per second or hertz. To limit bandwidth, filters may be applied; a low-pass filter limits the low frequencies, and baseband bandwidth is used to define the upper frequency limit.

The amplitude of a signal corresponds to the voltage, which is another way of describing the electrical "pressure" or potential energy at the point the voltage is measured. As the signal travels down the wire, the signal encounters resistance in the wire, and some of the potential energy is converted to kinetic energy. Heat is produced and the signal strength is degraded. This is one of the reasons why there are length limitations on different types of cables and technologies. Frequency has a direct relationship to energy. The physicist Max Planck found that the energy of a photon could be determined using the following formula:

```
E = h ν
```

where h is Planck's constant and ν, or Nu, is the frequency. The higher the frequency, the higher the energy. Planck's law doesn't apply to the energy of electrons in a wire, but the overall effect of energy loss is to diminish the highest-frequency waves first.

If you analyze signal loss, there is usually a frequency above which the signal drops off rapidly. This is called the *cutoff frequency*. You can also achieve a cutoff by introducing a low-pass filter in the circuit. Low-pass filters are used to limit the bandwidth of a circuit. A low-pass filter reduces noise in signals and allows higher frequencies to be boosted so that their signal-to-noise ratios are higher and it is easier to send a higher frequency of data over a circuit.

The impact of a filter that allows only very low frequencies to pass through it is that only the first harmonic term in the Fourier series may pass through the filter. If that is the case, then the signal is quite degraded and becomes unusable. As the filter limit is raised to higher frequencies, more terms in the Fourier series pass through the filter, and the signal more accurately represents the original signal. In [Figure 5.4](ch05.html#sampling_a_sine_curve_and_the_nyquist_sa), raising the pass-through frequency would first let the k = 5 term through; raising it some more would let the k = 15 term contribute.

Noise, resistance, contention, and other factors always place a limit on the frequency of the signal that can pass through the wire. The rate of change per second is called the *baud rate*. In the examples you've seen so far, the amplitudes were normalized to a value of 1. However, if the voltage were high enough to represent intermediate values, then the baud rate would have to account for voltage changes as well. In a system where the signal is at a voltage that allows two logical values, 1 and 2, to be determined, each signal carries two bits worth of information and the baud rate is twice what it would be for a system of just 1 and 0.

## Sampling theory

In the previous sections, you saw how you could take a digital signal and describe it in terms of periodic trigonometric functions, such as sinusoids. You also saw how the signal could encode data (ones and zeros) that could be used to convey information (SOS). The process of splitting up data into bits of information is called *sampling*, and the number of bits of information per unit time is the *sampling rate*.

The information contained within a single data point is a function of the bit space. Let's say that you have a signal that changes color in a periodic way and it is the color value that conveys information. The first system you build changes color from black to white through continuous shades of gray. Because the human mind can only differentiate around 1,000 shades of gray under ideal situations, you decide to store the color value at 256 different levels. That corresponds to an 8-bit data point.

The second system is a full-color system. To represent a color value in time, you might describe the color using the RGB (Red, Green, and Blue) color space. For each color, you choose a scale of 256 values, just as you did with the grayscale system. Now you have a bit depth that is 256 × 256 × 256 (28 × 28 × 28) or 224. This color space stores approximately 16.8 million color values. You could have used smaller or larger bit depths, and whether you did so would depend upon the purpose you intended to use the data for.

Sound or music can be sent over a wire and displayed as an analog signal in a waveform. You might ask the question: "How many data samples are required?" The answer again depends upon your intended purpose. For conversations over a telephone, a sampling rate of 8 kHz is sufficient. Higher-quality speech might be recorded at 11 kHz. For music, you might store a signal of lower quality such as AM radio at 22 kHz, while for CD quality, the sampling rate would be 44 kHz.

Now let's consider the sine wave shown in [Figure 5.4](ch05.html#sampling_a_sine_curve_and_the_nyquist_sa). How many samples do you need to take in order to determine its frequency? If you sample at once a cycle, and then try to reconstruct the waveform, what you get is a constant value that defines a line. If you increase the sampling rate to 1.5 samples per cycle, you get a sine wave, but at a lower frequency than the sine wave you are trying to describe. At two samples per cycle, you are finally able to store the frequency rate. To better approximate the waveform, you need to sample at least twice the maximum frequency, but the more samples you take, the closer you are to recreating the original sine wave. At 16 samples per cycle, you are close to recreating the original sine wave.

[Figure 5.4](ch05.html#sampling_a_sine_curve_and_the_nyquist_sa) shows that at twice the rate of the sine wave, you can store the information necessary to define the frequency. This rate is known as the *Nyquist rate*, and it comes from the 1924 work of Harry Nyquist. He found that you can have a signal with a bounded bandwidth B, and that the signal can be recreated by storing 2B samples per second, which is the *Nyquist frequency*. The original work was with a low-pass filtered signal over a noiseless channel. The reason why a higher sampling rate is oversampling and yields no additional information is because higher frequencies have already been eliminated when they were filtered out.

Nyquist's theorem for the relationship of the bandwidth B to the maximum sampling rate R is as follows:

```
Rs = 2Blog2 BL
```

where BL is the number of values that a bit can have. A voice signal of 262 Hz is C4 or Middle C and is considered the median note of a human voice. The Nyquist theorem calculated that a maximum sampling rate to store this note in digital form (BL = 2) would be 524 bits/s.

![Sampling a sine curve and the Nyquist sampling rate](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0504.png)

**Figure 5.4. Sampling a sine curve and the Nyquist sampling rate**

In 1948 Claude Shannon published a paper that provided a mathematical proof for Nyquist's theorem and went on to extend the concept by showing that you could reconstruct the original signal from 2B samples. Put another way, sending a signal with a baud rate of 2B is the inverse operation of sampling a signal with a frequency of 2B. The resulting theorem is now referred to as the *Nyquist-Shannon sampling theorem*, and Shannon's work is considered by many scholars as marking the beginning of the field of science known as information theory.

The sampling theorem applies to a noiseless channel. Most channels do suffer from noise and the noise introduces a certain degree of randomness to the data. The amount of noise in a signal is given by the ratio of the power of the signal to the noise, S/N. Because noise is often a minor component of the signal, it is common to quote the S/N ratio as a function of the common log, 10log10 S/N in units of decibels. An antenna that attenuates the noise of a receiver by 10 dB would reduce the noise in the signal by a factor of 10. A fine stereo cartridge that has a 75 dB S/N ratio would have a signal-to-noise ratio of 750 to 1.

Shannon went on to establish that you could calculate the maximum sampling rate for a noisy channel by substituting the term 1 + S/N into the Nyquist theorem for the bit level, as follows:

```
Rs = Blog2 (1 + S/N)
```

The effect of noise comes into play when you are trying to determine the maximum amount of information that a channel can transmit. Consider a channel with a low-pass filter that cuts off all frequencies at about 1000 Hz, and which is subject to Gaussian thermal noise. The S/N ratio is 20 dB; and S/N would be 200/1. Therefore, Rs is calculated to be:

```
Rs = 1000 log2 (1 + 200) = 1000 * 5.30 = 5300 bits/s
```

This calculation shows that the channel described can transmit signals at a maximum rate of 5300 bits/s, regardless of the sampling rate, under ideal conditions. An important realization is that the amount of information conveyed is much more sensitive to the frequency of the signal than it is to the quality of the signal (S/N).

Information theory goes on to relate the assignment of values to signals as a form of negative entropy. That is, a logical sequence of bits requires some energy to be in that state instead of being randomly assigned as it would in a thermal state. Therefore, any data claimed above the maximum Shannon sampling rate would be akin to creating energy. As interesting as this idea might be, the point is that this theory establishes a theoretical maximum data rate for any channel.

# Multiplexing

The process by which a transmission medium can be made to carry two or more signals or data streams is called *multiplexing*. Conceptually, a multiplexed transmission is carried over a channel, and the path a channel takes from one point to another describes a circuit. Because a wire, fiber, or radio link is a physical connection that is described as a physical circuit, data channels are often referred to as *virtual circuits*.

Multiplexing requires a device called a *multiplexer* (MUX) that is capable of both separating and combining multiple signals or data streams into individual channels. The multiplexer device is actually a combination of a multiplexer that takes multiple inputs and combines them, and a demultiplexer (DEMUX) that separates the signals into components and sends each signal down the appropriate output.

Previously you learned that there are three different methods used to modulate carrier waves so that they encode data: amplitude modulation, frequency modulation, and phase modulation. Similarly, multiplexers perform time, frequency, or phase division (partitioning) of analog and digital data. These classifications separate one set of computer protocols from another, and one type of computer network from another, in the same way that Linnaean taxonomy allows biologists to separate the tree of life into a hierarchy of domains, then kingdoms, phyla or divisions, families, genera, and species.

## Time Division Multiplexing

Time-based multiplexing is referred to as *Time Division Multiplexing* (TDM) and uses time slicing to separate data streams. When different transmitters share the same TDM network, the technology is referred to as *Time Division Multiple Access* (TDMA).

TDM sequences analog data using a device called a *codec*, which samples the data into a stream. At the receiving end, a codec reassembles the data from the slices. You are probably familiar with codecs, as they are used to digitize voice, music, and video, another example of this technology. This kind of sampling is referred to as *Pulsed Code Modulation* (PCM). Other techniques, such as *Pulsed Amplitude Modulation* (PAM), *Pulsed Width Modulation* (PWM), and *Pulsed Position Modulation* (PPM), are used less frequently than PCM to perform digital modulation.

TDM uses different techniques to sequence digital data. The system used on T- and E-carrier lines multiplexes a set of channels together, whereas TDM transmits the multiplexed channels as one large frame consisting of multiple channels (25 for T-1) every 125 (sec. There are different standards for TDM frame sequences that add control bits either to the end of the channels (*common channel signaling*) or to the end of the frames (*channel associated signaling*). Channel signaling uses the same time slicing technique shown in [Figure 5.5](ch05.html#a_comparison_of_time_division_multiplexi) for TDM, but instead of sending a sequence of channels, it sends a sequence of frames.

### Note

T- and E-carrier lines are discussed in [Chapter 13](ch13.html).

There are many different methods used to compress digital data that is being time multiplexed; some are industry standards, and others are proprietary. One common technique for compression is called *differential pulsed code modulation*. This technique evaluates the amplitude of time slices and determines the difference or delta value between that time slice and the next time slice. The codec sends a data stream consisting of the delta values only. You get data compression because the delta is assumed to never go beyond a certain value. When the sound does vary widely between time slices, the compression scheme uses the next time slices to bring the levels in line with the original waveform.

For example, in a system that stores 256 sound levels, which is 28, you might decide that the levels never change more than 8 levels in any one time slice. Instead of encoding an 8-bit signal, this system would allow you to send only 7 bits of information per slice.

The technique called *delta modulation* stores only step changes of 1 in the value as a single bit. Delta modulation requires a very fast sampling rate in order to accurately describe the original waveform. Other more advanced compression schemes use algorithms to do predictive encoding. You can more aggressively compact signals, but there is a cost in data quality or more overhead to process data more quickly.

## Frequency Division Multiplexing

Frequency-based multiplexing uses signal modulation to separate one signal from another; and is referred to as *Frequency Division Multiplexing* (FDM). When a single channel is shared between users using FDM the technology is referred to as Frequency Division Multiple Access. FDMA is used to keep radio signals coming from different transmitters apart, and because cellular telephone networks are designed to have overlapping ranges FDMA finds use in cellular networks.

FDM multiplexing can send either analog or digital data, but as a general rule, it is easier to send digital data over TDM circuits and it is easier to send analog data over FDM circuits. FDM networks are found in wired networks and in microwave technologies. FDM is used on all sorts of wired media, but when frequency modulation is used on fiber-optic lines it is called Wavelength Division Multiplexing (WDM), although they are essentially the same idea. TDM multiplexing is really only practical for carrying digital data.

[Figure 5.5](ch05.html#a_comparison_of_time_division_multiplexi) shows a simple example of TDM and FDM. The channels are indicated by the numbers in the boxes. In TDM, channels pass by oscillating between channel 1 and channel 2. The overall data stream is fully utilized, and consists of consecutive packets filling the channels during each time slice. In FDM, the channels are separated into four separate frequency channels and data is alternately sent over each of them.

In FDM although there are guard bands between each of the frequencies in the figure, in real life, many transmission schemes crowd channels together so that they overlap a little. There can also be overlap due to the fact that band filters usually create a sharp edge on a channel. The guard bands are represented by the blank spaces between each of the four frequency channels.

### Tip

In FDM, a group is usually considered to be a 4000 Hz band that includes 500 Hz blank guard bands at the start and end of the group. This corresponds to the bandwidth required to carry voice data. A set of five groups is a *supergroup*, and a *mastergroup* is either five or ten supergroups.

![A comparison of Time Division Multiplexing versus Frequency Division Multiplexing](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0505.png)

**Figure 5.5. A comparison of Time Division Multiplexing versus Frequency Division Multiplexing**

## Other multiplexing technologies

Because wavelength and frequency are fundamentally related by the speed of light, you might think that FDM would also be used in optical networks. However, for historical reasons, optical networks refer to frequency multiplexing as *Wavelength Division Multiplexing* (WDM).

You can create a WDM link by placing optical fibers on one side of a prism so that different frequency ranges of light travel down different fibers. The other side of the prism would combine the light so that it travels down a shared optic fiber link. [Figure 5.6](ch05.html#wavelength_division_multiplexing_beam_sp) shows how WDM is achieved using a prism or a diffraction grating.

### Note

[Chapter 13](ch13.html) describes the use of multiplexing for internetwork links and the protocols that use those techniques.

![Wavelength Division Multiplexing beam splitting and recombination](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0506.png)

**Figure 5.6. Wavelength Division Multiplexing beam splitting and recombination**

You encounter multiplexing techniques that polarize a data stream in some optical networks. Light can be polarized in a number of different ways, but one common technique is to use an *Add-Drop Multiplexer* (ADM). ADMs typically use a Fabry-Pérot etalon (interferometer) to split or combine light waves. More recent versions of ADMs, called *Reconfigurable Optical Add-Drop Multiplexers* (ROADMs), have become popular on *Metropolitan Area Networks* (MANs). Not all optical networks use polarization. The widely used SONET/SDH optical network uses timed pulses of lasers and LEDs to create TDM communications.

*Radio frequency communications* can be polarized by passing the data through a phased multi-antenna array to create *Multiple-Input and Multiple-Output* (MIMO) channels. The signal is recombined at a receiving phased multi-antenna array. This technology is similar to the way RADAR is created. MIMO wireless networks are becoming more popular in home wireless networks in order to create higher throughput connections.

### Note

Just to make this nomenclature even more confusing, radio frequency multiplexing uses the FDM acronym.

Other forms of multiplexing exist that are important in areas such as cellular communications. *Frequency-hopping spread spectrum* (FHSS) radio communications is perhaps the most famous of these methods. This multiplexing technology works by rapidly switching the carrier wave between a number of different frequencies in a pseudorandom sequence. The transmitting device and receiving device are aware of the order and timing and can tune in, but a spread spectrum transmission would simply appear as transient noise to any narrowband receiver that is tuned to any one frequency. This makes FHSS very secure.

A famous patent in frequency hopping was issued to the composer George Antheil and the actress Hedy Lamarr in 1942 for a system that used a piano roll to switch between 88 different radio frequencies. It was hoped that this system would make it impossible to jam radio-guided torpedoes. The system was never deployed, but became widely known when the *Code Division Multiple Access* (CDMA) system for cellular networks was developed a decade later.

# Flow Control

As data flows across a network, there is often a mismatch between the rate at which a system can process data and the rate at which data is being received. These mismatches occur when the receiving system is slower to process and/or cache incoming data than the sending system is at sending the data through the network connection. When the receiving system is the target of data coming in from multiple systems, it's even easier to get a data transfer/processing mismatch. Yet another problem is encountered when a network segment becomes congested, and packets or frames required by the receiving system to reassemble the data cannot be acquired in a timely fashion. The management of data traffic is a problem that is typically addressed in Session layer (Level 3 in the OSI model) protocols using flow control messaging, data caching, session timing schemes, data buffering, and other techniques.

Network flow control can be implemented by devices referred to as *Data Terminal Equipment* (DTE), at switches and routers, and at the circuit level using *Data Circuit Terminating Equipment* (DCE). These devices control the transmission of data by providing a gating function that alters the rates of data flow in one direction or in the opposite direction. A connection must have one of these DTEs or DCEs at each endpoint.

Modems are devices that suffer from flow control problems. A modem negotiates a connection with another modem, ensuring a certain set of protocols are used for the session, a certain data transfer rate, and so on. Modern high-speed modems, at 56 Kbits/s, transfer data at a rate that exceeds the theoretical Nyquist rate when they operate at full speed. They do so by employing compression and other techniques. Data transfer using modems over phone lines have a theoretical limit of around 56 Kbps (the bandwidth of the DS0 telephone channel), but with compression and error correction it is possible to transfer data at a slightly faster rate if the phone line is sufficiently free of noise. However, phone line quality can vary — often by a large amount — and so some mechanism needs to be employed to signal the current condition of the telephone line and the amount of noise that might be encountered. That mechanism is to go through a handshaking routine where the transfer rate and different protocols are negotiated by both the sending and receiving modem.

Most modems use two different forms of flow control. The first method is a set of commands called XON/XOFF that are sent from the modem to the computer. The program that your computer is using to communicate with the modem can also send XON/XOFF messages to the modem. This form of flow control is called *software flow control* (modems can be implemented in software). When a connection is made without a feedback loop like these commands do, it is a form of open-loop flow control. An open-loop flow control mechanism doesn't use communication between the sender and receiver, relying instead on other flow control mechanisms such as resource allocation using resource reservations. You see this type of flow control in ATM networks.

The second system uses control characters or RS 232 and serial port control lines to send control signals and is called *hardware flow control*. Common control signals are *DTR* (Data Terminal Ready), *DSR* (Data Set Ready), *CTS* (Clear to Send), and *RTS* (Request to Send). These are signals that you may see indicated by a set of lights on physical modems. Hardware flow control uses a master/slave relationship. The DTE master sends a signal indicating its condition; then the DCE slave responds. A PC modem connection uses DTR/DSR signals to create a modem session and RTS/CTS signals to control data transfer.

Flow control is also built directly into important protocols. The Internet Protocol (a Network level protocol in the OSI model or the main protocol at the Internet level in the TCP/IP Internet model) creates IP packets that contain blocks that provide a sequence number for reassembly, blocks that indicate packet priority, and so forth. As packets arrive, messages are sent back to indicate if there are any missing packets that are required, if a packet failed its error check, and if a packet took too long to arrive, and when the data has been reassembled completely then the transfer was received correctly. The use of messaging is a form of closed-loop flow control.

The IP protocol is not unique in using a messaging system or in signaling the successful transfer of data. The Frame Relay network protocol (a Data Link protocol), which is used to connect LANs to WANs, creates frames that encapsulate data from packets in the form of variable-sized frames. Frame relay technology has no flow control or acknowledgment messaging. However, frame relay networks offer congestion control for incoming connections and guaranteed throughput mechanisms. Two different control bits in the data header tell the sender when there is congestion, and the sending system reads those bits and adjusts the data rate.

# Traffic Engineering

Traffic engineering describes a set of technologies that are used to control traffic on packet-switched networks such as TCP/IP or the Internet. Among the technologies that are used are *packet shaping* (where packets are controlled based on their type of content), *store and forward technologies* (exemplified by the Leaky Bucket Algorithm), and *buffering technologies* (such as the Token Bucket Algorithm). All of these technologies are flow control methods that are used to enforce different Quality of Service levels that both filter and meter network bandwidth to clients.

## Packet shaping

A common method that is used to control data rates on a network is called *traffic shaping*, or on an IP network, it is more frequently called *packet shaping*.

Packet shaping isn't just a flow control mechanism that controls data transfer rates. Packets can be categorized on the basis of the protocol they use or the port number that they are destined for. Based on these parameters, rules can be established that alter the way the packets are handled. For example, one ISP examines packets, and if they find that they are BitTorrent packets, they apply a low *Quality of Service* (QoS) to them and send them down the wire as a trickle. BitTorrent can be easily recognized by the fact that the header begins with the character 19 and a 19-byte handshake string.

If a packet is analyzed as part of a *Voice over IP* (VoIP) data stream, then it can be prioritized by an ISP to ensure a certain QoS level. Another ISP (a large phone company, for example) might choose to lower the QoS level so that VoIP doesn't seem as attractive as their phones. This happens to Skype traffic on some networks or to video streaming on networks that are provided by a large cable ISP.

Packet shaping, like any tool, can be used for good reasons or not-so-good reasons. However, without some form of packet shaping, it would be impossible for large public networks to provide the QoS that their service agreements contractually commit them to.

On ATM networks, cells are examined using an algorithm called the *Generic Cell Rate Algorithm* (GCRA) and checked for their compliance to rules that are defined for that particular virtual circuit. A cell is a small, specially formatted packet of data that is transferred on ATM networks and other similar cell relay technologies. Depending upon the arrival rate and variance in that rate, cells are passed through, scheduled, or dropped. GCRA changes the flow control bit settings in the ATM cells to change the data rate. Techniques such as *admission control, resource reservation*, and *rate-based congestion control* are used by ATM networks to control traffic flow.

### Note

Cells are described in more detail in [Chapter 13](ch13.html).

Admission control is a mechanism for assigning network bandwidth and latency to different types of traffic entering a network. Resource reservation refers to a system by which network resources are set aside for different application data streams and is commonly used for broadcast technologies. Rate-based congestion control is a technique similar to the traffic light controlled entry lanes on freeways: traffic is allowed onto the network at a steady rate in order to limit network congestion.

On IP networks, packet shaping examines the headers of packets that are flowing through an IP connection, and if the packets match some criteria that you set a rule for, it executes that rule. Packet shaping can limit the bandwidth allowed to a certain datatype or bound to a certain IP address, which is called *bandwidth throttling*. Packet shaping can also be used to change the allowed rate of data transfer and to delay or redirect traffic. *Traffic policing* is differentiated from packet (traffic) shaping in that traffic policing drops packets or marks them.

As you can imagine, packet shaping is a very popular technology with ISPs, who refer to the technology as *network traffic engineering*. You can think of packet shaping as a "Quality of Service" technology if you like, and ISPs tend to describe it in those terms.

Packet shaping is enabled in application software usually running on a network edge device. Some companies, such as Packeteer, offer a PacketShaper appliance. The PacketShaper appliance enforces the various Quality of Service technologies described in the sections on traffic engineering. Packeteer was acquired by Blue Coat Systems in June 2008 (`www.bluecoat.com`).

## Leaky Bucket algorithm

Packet shapers use different methods to store and forward packets. A common scenario places ATM cells or IP packets into a buffer and then uses an algorithm to determine how to transmit them. The buffer, often referred to as a *bucket* in this technology, may use a delay technique or *Leaky Bucket* to create a First In First Out mechanism that takes an inflow at a variable rate and then transmits the data at a fixed (usually lower) rate.

The effect is similar to having some small holes in the bottom of a bucket and then filling the bucket up with water. A packet shaper can control the size of the "holes" of the bucket, and thus the outgoing rate. If the incoming rate overflows the buffer, then the packets flow over the top of the bucket, and they are discarded. [Figure 5.7](ch05.html#the_leaky_bucket_algorithm_provides_cons) shows the concept behind the Leaky Bucket.

![The Leaky Bucket algorithm provides constant data output.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0507.png)

**Figure 5.7. The Leaky Bucket algorithm provides constant data output.**

The Leaky Bucket algorithm is simple to implement when the sizes of the incoming packets are constant, the incoming rate is predictable, and the outgoing rate can be efficiently satisfied by the packet size in the bucket. However, in situations where the packet size varies or the incoming rate is bursty (subject to short spurts of high traffic volume), the Leaky Bucket algorithm has a number of inefficiencies, most notably the fact that when high traffic is encountered that is beyond the capacity of the bucket, that extra traffic is discarded. Modifications to the Leaky Bucket that add a byte-counting algorithm improve the Leaky Bucket algorithm's performance.

## Token Bucket algorithm

A second buffer mechanism used is called a *Token Bucket*. This packet shaping flow control uses an algorithm that can control how much data is allowed onto the network, and provides the byte-counting capabilities that the Leaky Bucket lacks. The algorithm provides for average and burst transfer rates. Whereas the Leaky Bucket enforces a constant outgoing rate, the Token Bucket allows for more flexibility in the data rate.

The token mechanism acts as follows: A bucket is filled with tokens, which represent an amount of data that can be sent. When data is removed, the token that corresponds to that amount of data is removed from the bucket. When all tokens are gone, data is not transmitted. If there are enough tokens in the bucket, then the data can be transmitted at a bursty rate. If the bucket is full of tokens, then any additional tokens are discarded. These four scenarios are illustrated in [Figure 5.8](ch05.html#the_token_bucket_algorithm_provides_vari).

In this system, a network administrator assigns how many tokens correspond to how many bytes of data. There is a constant rate of new tokens arriving at the bucket, but the bucket has a limited capacity. When a packet arrives of a certain size, the number of tokens required for that size are removed. If a packet arrives and there aren't enough tokens, then the packet is dropped, held in a buffer, or marked and transmitted.

![The Token Bucket algorithm provides variable data output.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0508.png)

**Figure 5.8. The Token Bucket algorithm provides variable data output.**

# Quality of Service

Quality of Service (QoS) is a form of packet shaping or traffic engineering that guarantees that a certain service will have a certain amount of resources dedicated to it. The classic use of the term *QoS* is to ensure that an application that is in real time and sensitive to delays is given a certain sized circuit over which it can be transmitted. QoS is especially important for VoIP, streaming media, online multiplayer games, and other such applications. QoS methods are only employed when the network is bandwidth limited or congested. QoS technology is being built into network server operating systems such as Windows servers.

QoS is not a metric that is used to measure delays, latencies, signal-to-noise ratios, frequency response, and so on, although the QoS agreement can include these requirements. These sorts of metrics are better classified as a *Grade of Service* (GoS), with QoS reserved for resource access. The two concepts, although related, are often confused.

As an example of QoS services, let's take a look at how they are implemented using the *Asynchronous Transfer Mode* (ATM). ATM networks have several categories of service built into that transfer protocol. These categories are built directly into ATM network adapters and ATM switches to service different classes of subscribers.

Classes of ATM services that are available:

- **Constant Bit Rate (CBR)**. This category provides no control over traffic flow and no error checking. CBR is used on T1-carrier connections.
- **Unspecified Bit Rate (UBR)**. This category provides no congestion messaging and sets no flow level. Cells move about the ATM network up to the available capacity. When the capacity is exceeded, cells are discarded; if there is additional capacity, more cells are transferred. Any program that does its own flow control and error checking can use UBR. Typical applications that this category attracts are mail servers (e-mail) and FTP servers (background file transfers).
- **Real Time Variable Bit Rate (RT-VBR)**. This category is used for applications that deliver data in a form that is non-linear. An example would be videoconferencing, which, due to the way its compression works, creates frames in a non-linear way. RT-VBR ensures that there is enough data to provide the compression algorithm with an adequate queue to run the video smoothly or to ensure that the compression is efficiently used.
- **Non-Real Time Variable Bit Rate (NRT-VBR)**. Applications that require traffic flow control but can accommodate a certain amount of variability (called *jitter*) can use this category. Print spooling is an example of an application that can use NRT-VBR.
- **Available Bit Rate (ABR)**. This level of service allows data to move through the line at a rate that is dependent upon the available bandwidth. It is meant to accommodate bursty traffic and to allow network capacity to be better utilized at times when traffic is low. Web server traffic is an example of an application that can use the ABR service.

Network service providers may implement a service such as ABR when they have short periods of high utilization, as it can allow them to avoid building additional capacity when the investment isn't required long term. To implement ABR, a messaging system is implemented that informs sending systems when traffic is high and that they need to throttle their traffic back.

[Table 5.1](ch05.html#atm_service_categories) summarizes the different capabilities of ATM service categories.

**Table 5.1. ATM Service Categories**

|  | Bandwidth Control | Bursty Traffic (Variable) | Congestion Control | Real Time |
| --- | --- | --- | --- | --- |
| **ABR** | Capable | Yes | Yes | No |
| **CBR** | Yes | No | No | Yes |
| **NRT-VBR** | Yes | Yes | No | No |
| **RT-VBR** | Yes | No | No | Yes |
| **UBR** | No | Yes | No | No |

These different service categories allow ATM network service providers to create *Service Level Agreements* (SLAs) with their subscribers that guarantee access to network resources. The contracts contain a traffic description that may specify bandwidth and/or throughput values in a measurable way. Transfer rates may be measured for *Sustained Cell Rate* (SCR), *Peak Cell Rate* (PCR), *Minimum Cell Rate* (MCR), *Cell Error Rate* (CER), *Cell Loss Rate* (CLR), *Cell Transfer Delay* (CTD), *Severely Errored Cell Block Ratio* (SECBR), *Cell Delay Variation Tolerance* (CDVT), *Cell Delay Variation* (CDV), and *Cell Misinsertion Rate* (CMR). These parameters are measurable and are defined on a connection basis in ATM.

# Summary

In this chapter, you were introduced to signaling and information theory. These basic concepts are at the heart of why networks do what they do and how different types of networks are different from one another, and they separate what is possible to do on the network from what is impossible.

Complex data can be described in mathematical terms using techniques such as Fourier analysis. This allows you to store information and recreate the data at a later time. Sampling data provides the means to recreate data. There is a theoretical limit to the amount of sampling that is useful based on the bandwidth of the data.

Networks create channels that allow data streams to share network segments. Channels are created in a number of different ways, based on time, frequency, and polarity. The process of creating channels is called multiplexing, and when you combine data streams it is called demultiplexing.

Traffic control, flow control, and congestion control methods allow a network to provide services of different quality levels.

In the next chapter, you will learn about servers, systems, and appliances. These devices provide the important network services that clients and the network depend on.
