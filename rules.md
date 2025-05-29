# chiagent Project Rules and Guidelines

## Global Development Principles

### Code Quality
1. **Maintainability**
   - Write clean, modular code
   - Follow consistent naming conventions
   - Keep functions focused and small
   - Use meaningful variable names

2. **Documentation**
   - Document all public APIs
   - Include example usage
   - Keep READMEs up to date
   - Document complex logic

3. **Testing**
   - Write tests before code
   - Test edge cases
   - Maintain high coverage
   - Keep tests readable

4. **Version Control**
   - Commit atomic changes
   - Write clear commit messages
   - Use feature branches
   - Follow semantic versioning

## Project-Specific Rules

### Architecture
1. **Platform Integration**
   - Support Shopify and WooCommerce
   - Implement OAuth2 authentication
   - Use webhook subscriptions for real-time updates
   - Maintain separate sync jobs per platform

2. **API Design**
   - Follow RESTful principles
   - Support MCP protocol
   - Use consistent error handling
   - Implement rate limiting

3. **Data Management**
   - Use PostgreSQL for relational data
   - Implement Redis for caching
   - Maintain proper indexing
   - Normalize data models

### Features
1. **Product Discovery**
   - Implement NL query parsing
   - Support faceted search
   - Cache search results
   - Handle pagination

2. **Customer Service**
   - Implement refund workflows
   - Support address updates
   - Log all customer interactions
   - Validate order status

3. **Recommendations**
   - Analyze purchase history
   - Implement collaborative filtering
   - Cache recommendations
   - Track recommendation performance

4. **Virtual Try-On**
   - Handle selfie uploads
   - Integrate Google AI Mode
   - Cache overlay images
   - Implement image validation

### Development Workflow
1. **Sprint Structure**
   - 1-hour sprints
   - Clear deliverables
   - Timeboxed tasks
   - Regular retrospectives

2. **Code Review**
   - Review all changes
   - Check security implications
   - Verify test coverage
   - Ensure documentation

### Security
1. **Data Protection**
   - Encrypt sensitive data
   - Implement proper authentication
   - Use secure credential storage
   - Follow OWASP guidelines

2. **Access Control**
   - Implement proper authorization
   - Use rate limiting
   - Log security events
   - Regular security audits

## Best Practices

### Error Handling
- Never expose sensitive information
- Provide clear error messages
- Implement proper logging
- Use appropriate error codes

### Performance
- Optimize database queries
- Implement proper caching
- Monitor API performance
- Use efficient data structures

### Scalability
- Design for horizontal scaling
- Implement proper load balancing
- Use asynchronous processing
- Monitor resource usage

## Compliance

### Legal Requirements
- Follow GDPR requirements
- Implement proper privacy controls
- Document data processing
- Maintain audit trails

### Industry Standards
- Follow REST best practices
- Implement proper security protocols
- Use standard authentication methods
- Follow API documentation standards

## Communication

### Team Collaboration
- Maintain clear documentation
- Use consistent terminology
- Share knowledge regularly
- Document architectural decisions

### Stakeholder Communication
- Maintain clear progress reports
- Document technical decisions
- Share release notes
- Maintain API changelogs

## Technical Debt

### Management
- Document technical debt
- Prioritize debt reduction
- Track debt metrics
- Plan for refactoring

### Prevention
- Write maintainable code
- Implement proper testing
- Follow coding standards
- Review code regularly
