/**
 * Razorpay Payment Configuration
 * AKATRON - Email Risk Analysis Payment System
 */

const RAZORPAY_CONFIG = {
    // Live Razorpay Keys
    key_id: 'rzp_live_SBd4EDY4jkyuOv',
    
    // Business Details
    business_name: 'Akatron AI',
    business_logo: 'https://akatron-ai.github.io/akatron-website/akatron-logo.png',
    
    // Product Details
    products: {
        email_risk_basic: {
            name: 'Email Risk Analysis - Basic Report',
            amount: 49900, // ₹499 in paise (Razorpay uses smallest currency unit)
            currency: 'INR',
            description: 'Comprehensive email breach analysis with detailed report'
        },
        email_risk_premium: {
            name: 'Email Risk Analysis - Premium Report',
            amount: 99900, // ₹999 in paise
            currency: 'INR',
            description: 'Premium email security analysis with dark web monitoring'
        },
        osint_investigation: {
            name: 'OSINT Investigation',
            amount: 399900, // ₹3999 in paise
            currency: 'INR',
            description: 'Professional OSINT investigation service'
        }
    },
    
    // Payment Options
    payment_methods: {
        card: true,
        netbanking: true,
        wallet: true,
        upi: true,
        paylater: false
    },
    
    // Webhook URL (will be configured later)
    webhook_url: 'https://akatron-webhook.vercel.app/api/payment-success',
    
    // Contact Details
    contact: {
        email: 'arpitkatiayar261@gmail.com',
        phone: '' // Add your phone number
    }
};

/**
 * Initialize Razorpay Payment
 * @param {string} productKey - Product key from RAZORPAY_CONFIG.products
 * @param {string} customerEmail - Customer's email address
 * @param {function} onSuccess - Callback function on successful payment
 * @param {function} onFailure - Callback function on payment failure
 */
function initiatePayment(productKey, customerEmail, onSuccess, onFailure) {
    const product = RAZORPAY_CONFIG.products[productKey];
    
    if (!product) {
        console.error('Invalid product key:', productKey);
        if (onFailure) onFailure('Invalid product');
        return;
    }
    
    const options = {
        key: RAZORPAY_CONFIG.key_id,
        amount: product.amount,
        currency: product.currency,
        name: RAZORPAY_CONFIG.business_name,
        description: product.description,
        image: RAZORPAY_CONFIG.business_logo,
        
        // Prefill customer details
        prefill: {
            email: customerEmail,
            contact: RAZORPAY_CONFIG.contact.phone
        },
        
        // Payment methods
        config: {
            display: {
                blocks: {
                    banks: {
                        name: 'Pay using ' + product.currency,
                        instruments: [
                            {
                                method: 'card'
                            },
                            {
                                method: 'netbanking'
                            },
                            {
                                method: 'wallet'
                            },
                            {
                                method: 'upi'
                            }
                        ]
                    }
                },
                sequence: ['block.banks'],
                preferences: {
                    show_default_blocks: true
                }
            }
        },
        
        // Theme
        theme: {
            color: '#DAA520' // AKATRON gold color
        },
        
        // Success handler
        handler: function(response) {
            console.log('Payment successful:', response);
            
            // Payment details
            const paymentData = {
                razorpay_payment_id: response.razorpay_payment_id,
                razorpay_order_id: response.razorpay_order_id,
                razorpay_signature: response.razorpay_signature,
                customer_email: customerEmail,
                product_key: productKey,
                amount: product.amount / 100, // Convert back to rupees
                timestamp: new Date().toISOString()
            };
            
            // Track in Google Analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'purchase', {
                    transaction_id: response.razorpay_payment_id,
                    value: product.amount / 100,
                    currency: product.currency,
                    items: [{
                        item_name: product.name,
                        price: product.amount / 100,
                        quantity: 1
                    }]
                });
            }
            
            // Call success callback
            if (onSuccess) {
                onSuccess(paymentData);
            }
        },
        
        // Modal settings
        modal: {
            ondismiss: function() {
                console.log('Payment cancelled by user');
                if (onFailure) {
                    onFailure('Payment cancelled');
                }
            }
        }
    };
    
    // Create Razorpay instance and open checkout
    const rzp = new Razorpay(options);
    
    rzp.on('payment.failed', function(response) {
        console.error('Payment failed:', response.error);
        
        // Track failure in Google Analytics
        if (typeof gtag !== 'undefined') {
            gtag('event', 'payment_failed', {
                error_code: response.error.code,
                error_description: response.error.description
            });
        }
        
        if (onFailure) {
            onFailure(response.error);
        }
    });
    
    rzp.open();
}

/**
 * Quick payment for Email Risk Analysis
 * @param {string} email - Customer's email to analyze
 */
function payForEmailRiskAnalysis(email) {
    initiatePayment(
        'email_risk_basic',
        email,
        function(paymentData) {
            // Success - Show confirmation and trigger report generation
            showPaymentSuccess(paymentData);
            generateEmailReport(email, paymentData);
        },
        function(error) {
            // Failure - Show error message
            showPaymentError(error);
        }
    );
}

/**
 * Show payment success message
 */
function showPaymentSuccess(paymentData) {
    alert('✅ Payment Successful!\n\n' +
          'Payment ID: ' + paymentData.razorpay_payment_id + '\n' +
          'Amount: ₹' + paymentData.amount + '\n\n' +
          'Your detailed report will be sent to ' + paymentData.customer_email + ' within 5 minutes.');
}

/**
 * Show payment error message
 */
function showPaymentError(error) {
    if (error === 'Payment cancelled') {
        alert('Payment was cancelled. You can try again anytime.');
    } else {
        alert('❌ Payment Failed\n\n' + 
              (error.description || 'Please try again or contact support.'));
    }
}

/**
 * Generate and send email report (placeholder - will be implemented with backend)
 */
function generateEmailReport(email, paymentData) {
    console.log('Generating report for:', email);
    console.log('Payment data:', paymentData);
    
    // TODO: Implement backend API call to:
    // 1. Generate detailed PDF report
    // 2. Send email with report attachment
    // 3. Store payment record in database
    
    // For now, just log
    console.log('Report generation triggered');
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        RAZORPAY_CONFIG,
        initiatePayment,
        payForEmailRiskAnalysis
    };
}
